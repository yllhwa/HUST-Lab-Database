<script setup>
import { ref, reactive, onMounted, nextTick, h } from 'vue'

const columns = [
    {
        title: '学号',
        key: 'Sno',
    }, {
        title: '姓名',
        key: 'Sname',
    },
    {
        title: '性别',
        key: 'Ssex'
    },
    {
        title: '年龄',
        key: 'Sage'
    },
    {
        title: '系别',
        key: 'Sdept'
    },
    {
        title: '奖学金',
        key: 'Scholarship'
    }
]
const options = [
    {
        label: '新增',
        key: 'add',
    },
    {
        label: "编辑",
        key: "edit"
    },
    {
        label: () => h("span", { style: { color: "red" } }, "删除"),
        key: "delete"
    }
];

function query(page, pageSize = 8) {
    // /api/Students?page=1&size=8
    return fetch(`/api/Students?page=${page}&size=${pageSize}`)
        .then(res => res.json())
        .then(res => res.data)
        .then(res => {
            return {
                pageCount: res.pageCount,
                data: res.data,
                total: res.total
            }
        })
}

const dataRef = ref([])
const loadingRef = ref(true)
const columnsRef = ref(columns)
const paginationReactive = reactive({
    page: 1,
    pageCount: 1,
    pageSize: 8,
    prefix({ itemCount }) {
        return `总计: ${itemCount}`
    }
})

onMounted(() => {
    query(
        paginationReactive.page,
        paginationReactive.pageSize,
    ).then((data) => {
        dataRef.value = data.data
        paginationReactive.pageCount = data.pageCount
        paginationReactive.itemCount = data.total
        loadingRef.value = false
    })
})

let rowKey = (rowData) => {
    return rowData.column1
}

function handlePageChange(currentPage) {
    if (!loadingRef.value) {
        loadingRef.value = true
        query(
            currentPage,
            paginationReactive.pageSize
        ).then((data) => {
            dataRef.value = data.data
            paginationReactive.page = currentPage
            paginationReactive.pageCount = data.pageCount
            paginationReactive.itemCount = data.total
            loadingRef.value = false
        })
    }
}

// 模态框
const bodyStyle = {
    width: "600px"
}
const segmented = {
    content: "soft",
    footer: "soft"
}
let showModal = $ref(false)

const model_add = $ref({
    Sno: null,
    Sname: null,
    Ssex: null,
    Sage: null,
    Sdept: null,
    Scholarship: null
});

const model_edit = $ref({
    Sno: null,
    Sname: null,
    Ssex: null,
    Sage: null,
    Sdept: null,
    Scholarship: null
});

let addStudent = () => {
    // post /api/Students
    fetch("/api/Students", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(model_add)
    }).then(res => res.json())
        .then(res => {
            showModal = false
            nextTick(() => {
                handlePageChange(paginationReactive.page)
            })
        })
}

let editStudent = () => {
    // put /api/Students
    fetch("/api/Students", {
        method: "PUT",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(model_edit)
    }).then(res => res.json())
        .then(res => {
            showModal = false
            nextTick(() => {
                handlePageChange(paginationReactive.page)
            })
        })
}

let deleteStudent = () => {
    // delete /api/Students
    fetch("/api/Students", {
        method: "DELETE",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ "Sno": model_edit.Sno })
    }).then(res => res.json())
        .then(res => {
            showModal = false
            nextTick(() => {
                handlePageChange(paginationReactive.page)
            })
        })
}

// 右键功能
const showDropdownRef = ref(false);
const xRef = ref(0);
const yRef = ref(0);
let currentRow = $ref(null);
let currentKey = $ref(null);
const TitleMap = {
    "add": "新增",
    "edit": "编辑",
    "delete": "删除"
}
function handleSelect(key) {
    currentKey = key;
    showModal = true;
    showDropdownRef.value = false;
}
function onClickoutside() {
    showDropdownRef.value = false;
}

let rowProps = (row) => {
    return {
        onContextmenu: (e) => {
            currentRow = row;
            model_edit.Sno = row.Sno;
            model_edit.Sname = row.Sname;
            model_edit.Ssex = row.Ssex;
            model_edit.Sage = row.Sage;
            model_edit.Sdept = row.Sdept;
            model_edit.Scholarship = row.Scholarship;
            e.preventDefault();
            showDropdownRef.value = false;
            nextTick().then(() => {
                showDropdownRef.value = true;
                xRef.value = e.clientX;
                yRef.value = e.clientY;
            });
        }
    };
}
</script>

<template>
    <div style="height: 100vh; overflow-y: auto;">
        <n-data-table remote ref="table" :columns="columnsRef" :data="dataRef" :loading="loadingRef"
            :pagination="paginationReactive" :row-key="rowKey" @update:page="handlePageChange" :row-props="rowProps" />
        <n-dropdown placement="bottom-start" trigger="manual" :x="xRef" :y="yRef" :options="options"
            :show="showDropdownRef" :on-clickoutside="onClickoutside" @select="handleSelect" />
    </div>
    <n-modal v-model:show="showModal" class="custom-card" preset="card" :style="bodyStyle" :title="TitleMap[currentKey]"
        size="huge" :bordered="false">
        <div v-if="currentKey == 'add'">
            <n-form>
                <n-form-item label="学号">
                    <n-input v-model:value="model_add.Sno" @keydown.enter.prevent />
                </n-form-item>
                <n-form-item label="姓名">
                    <n-input v-model:value="model_add.Sname" @keydown.enter.prevent />
                </n-form-item>
                <n-form-item label="性别">
                    <n-input v-model:value="model_add.Ssex" @keydown.enter.prevent />
                </n-form-item>
                <n-form-item label="年龄">
                    <n-input v-model:value="model_add.Sage" @keydown.enter.prevent />
                </n-form-item>
                <n-form-item label="系别">
                    <n-input v-model:value="model_add.Sdept" @keydown.enter.prevent />
                </n-form-item>
                <n-form-item label="奖学金">
                    <n-input v-model:value="model_add.Scholarship" @keydown.enter.prevent />
                </n-form-item>
                <n-button :disabled="model_add.Sno === null" round type="primary" @click="addStudent">
                    确认
                </n-button>
            </n-form>
        </div>
        <div v-else-if="currentKey == 'edit'">
            <n-form>
                <n-form-item label="学号">
                    <n-input v-model:value="model_edit.Sno" @keydown.enter.prevent />
                </n-form-item>
                <n-form-item label="姓名">
                    <n-input v-model:value="model_edit.Sname" @keydown.enter.prevent />
                </n-form-item>
                <n-form-item label="性别">
                    <n-input v-model:value="model_edit.Ssex" @keydown.enter.prevent />
                </n-form-item>
                <n-form-item label="年龄">
                    <n-input v-model:value="model_edit.Sage" @keydown.enter.prevent />
                </n-form-item>
                <n-form-item label="系别">
                    <n-input v-model:value="model_edit.Sdept" @keydown.enter.prevent />
                </n-form-item>
                <n-form-item label="奖学金">
                    <n-input v-model:value="model_edit.Scholarship" @keydown.enter.prevent />
                </n-form-item>
                <n-button :disabled="model_edit.Sno === null" round type="primary" @click="editStudent">
                    确认
                </n-button>
            </n-form>
        </div>
        <div v-else-if="currentKey = 'delete'">
            <n-form>
                <div class="pb-4">确认要删除吗？</div>
                <n-button round type="error" @click="deleteStudent">
                    确认
                </n-button>
            </n-form>
        </div>
    </n-modal>
</template>

<style scoped>
</style>