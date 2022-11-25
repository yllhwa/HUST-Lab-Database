<script setup>
import { reactive } from 'vue'
let stat = reactive({
    average_grade: 0,
    excellent_rate: 0,
    fail_count: 0,
    max_grade: 0,
    min_grade: 0,
});

let deptRef = $ref(null);

let handleGetStat = () => {
    fetch("/api/stat?dept=" + deptRef)
        .then((res) => res.json())
        .then((res) => res.data)
        .then((data) => {
            stat.average_grade = data.average_grade;
            stat.excellent_rate = data.excellent_rate;
            stat.fail_count = data.fail_count;
            stat.max_grade = data.max_grade;
            stat.min_grade = data.min_grade;
        });
}
</script>

<template>
    <n-card title="统计数据">
        <n-form inline>
            <n-form-item label="系名">
                <n-input v-model:value="deptRef" placeholder="输入系名" />
            </n-form-item>
            <n-form-item>
                <n-button attr-type="button" @click="handleGetStat">
                    获取
                </n-button>
            </n-form-item>
        </n-form>
        <n-statistic label="平均成绩">
            {{ stat.average_grade }}
        </n-statistic>
        <n-statistic label="最好成绩">
            {{ stat.max_grade }}
        </n-statistic>
        <n-statistic label="最差成绩">
            {{ stat.min_grade }}
        </n-statistic>
        <n-statistic label="优秀率">
            {{ stat.excellent_rate * 100 }}%
        </n-statistic>
        <n-statistic label="不及格人数">
            {{ stat.fail_count }}
        </n-statistic>
    </n-card>
</template>

<style scoped>
</style>
