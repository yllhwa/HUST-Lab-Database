<script setup>
import { ref, reactive, onMounted, nextTick, h } from 'vue'

const columns = [
    {
        title: '课程号',
        key: 'Cno',
    }, {
        title: '课程名',
        key: 'Cname',
    },
    {
        title: '先导课程',
        key: 'Cpno'
    },
    {
        title: '学分',
        key: 'Ccredit'
    },
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
    // /api/Courses?page=1&size=8
    return fetch(`/api/Courses?page=${page}&size=${pageSize}`)
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
    Cno: null,
    Cname: null,
    Cpno: null,
    Ccredit: null
});

const model_edit = $ref({
    Cno: null,
    Cname: null,
    Cpno: null,
    Ccredit: null
});

let addCourse = () => {
    // post /api/Courses
    fetch("/api/Courses", {
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

let editCourse = () => {
    // put /api/Courses
    fetch("/api/Courses", {
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

let deleteCourse = () => {
    // delete /api/Courses
    fetch("/api/Courses", {
        method: "DELETE",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ "Cno": model_edit.Cno })
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
            model_edit.Cno = row.Cno;
            model_edit.Cname = row.Cname;
            model_edit.Cpno = row.Cpno;
            model_edit.Ccredit = row.Ccredit;
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
                <n-form-item label="课程号">
                    <n-input v-model:value="model_add.Cno" @keydown.enter.prevent />
                </n-form-item>
                <n-form-item label="课程名">
                    <n-input v-model:value="model_add.Cname" @keydown.enter.prevent />
                </n-form-item>
                <n-form-item label="先修课程号">
                    <n-input v-model:value="model_add.Cpno" @keydown.enter.prevent />
                </n-form-item>
                <n-form-item label="学分">
                    <n-input v-model:value="model_add.Ccredit" @keydown.enter.prevent />
                </n-form-item>
                <n-button :disabled="model_add.Cno === null" round type="primary" @click="addCourse">
                    确认
                </n-button>
            </n-form>
        </div>
        <div v-else-if="currentKey == 'edit'">
            <n-form>
                <n-form-item label="课程号">
                    <n-input v-model:value="model_edit.Cno" @keydown.enter.prevent />
                </n-form-item>
                <n-form-item label="课程名">
                    <n-input v-model:value="model_edit.Cname" @keydown.enter.prevent />
                </n-form-item>
                <n-form-item label="先修课程号">
                    <n-input v-model:value="model_edit.Cpno" @keydown.enter.prevent />
                </n-form-item>
                <n-form-item label="学分">
                    <n-input v-model:value="model_edit.Ccredit" @keydown.enter.prevent />
                </n-form-item>
                <n-button :disabled="model_edit.Cno === null" round type="primary" @click="editCourse">
                    确认
                </n-button>
            </n-form>
        </div>
        <div v-else-if="currentKey = 'delete'">
            <n-form>
                <div class="pb-4">确认要删除吗？</div>
                <n-button round type="error" @click="deleteCourse">
                    确认
                </n-button>
            </n-form>
        </div>
    </n-modal>
</template>

<style scoped>
</style>