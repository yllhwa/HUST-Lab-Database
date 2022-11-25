<script setup>
import { reactive } from 'vue'
let stat = reactive({
    detail: {
        "Sage": 0,
        "Scholarship": "?",
        "Sdept": "?",
        "Sname": "?",
        "Sno": "?",
        "Ssex": "?"
    },
    courses: []
});

let SnoRef = $ref(null);

let handleGetDetail = () => {
    fetch("/api/search?Sno=" + SnoRef)
        .then((res) => res.json())
        .then((res) => res.data)
        .then((data) => {
            stat.detail = data.detail;
            stat.courses = data.courses;
        });
}
</script>

<template>
    <n-card title="统计数据">
        <n-form inline>
            <n-form-item label="学号">
                <n-input v-model:value="SnoRef" placeholder="输入学号" />
            </n-form-item>
            <n-form-item>
                <n-button attr-type="button" @click="handleGetDetail">
                    获取
                </n-button>
            </n-form-item>
        </n-form>
        <n-statistic label="姓名">
            {{ stat.detail?.Sname }}
        </n-statistic>
        <n-statistic label="性别">
            {{ stat.detail?.Ssex }}
        </n-statistic>
        <n-statistic label="年龄">
            {{ stat.detail?.Sage }}
        </n-statistic>
        <n-statistic label="学院">
            {{ stat.detail?.Sdept }}
        </n-statistic>
        <n-statistic label="奖学金">
            {{ stat.detail?.Scholarship }}
        </n-statistic>
        <n-table :bordered="false" :single-line="false">
            <thead>
                <tr>
                    <th>课程号</th>
                    <th>课程名</th>
                    <th>成绩</th>
                    <th>学分</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="course in stat.courses" :key="course.Cno">
                    <td>{{ course.Cno }}</td>
                    <td>{{ course.Cname }}</td>
                    <td>{{ course.Grade }}</td>
                    <td>{{ course.Ccredit }}</td>
                </tr>
            </tbody>
        </n-table>
    </n-card>
</template>

<style scoped>
</style>
