import { createRouter, createWebHashHistory } from "vue-router";
import Index from "./pages/Index.vue";
import Students from "./pages/Students.vue";
import Courses from "./pages/Courses.vue";
import Grades from "./pages/Grades.vue";
import Stat from "./pages/Stat.vue";
import Rank from "./pages/Rank.vue";
import Search from "./pages/Search.vue";

import {
  HomeOutlined,
  PeopleAltOutlined,
  LibraryBooksOutlined,
  AutoAwesomeOutlined,
  AssessmentOutlined,
  AutoGraphOutlined,
  SearchOutlined,
} from "@vicons/material";

const routes = [
  {
    path: "/",
    name: "index",
    meta: {
      title: "主页",
      icon: HomeOutlined,
    },
    component: Index,
  },
  {
    path: "/students",
    name: "students",
    meta: {
      title: "学生管理",
      icon: PeopleAltOutlined,
    },
    component: Students,
  },
  {
    path: "/courses",
    name: "courses",
    meta: {
      title: "课程管理",
      icon: LibraryBooksOutlined,
    },
    component: Courses,
  },
  {
    path: "/grades",
    name: "grades",
    meta: {
      title: "成绩管理",
      icon: AutoAwesomeOutlined,
    },
    component: Grades,
  },
  {
    path: "/stat",
    name: "stat",
    meta: {
      title: "成绩统计",
      icon: AssessmentOutlined,
    },
    component: Stat,
  },
  {
    path: "/rank",
    name: "rank",
    meta: {
      title: "成绩排名",
      icon: AutoGraphOutlined,
    },
    component: Rank,
  },
  {
    path: "/search",
    name: "search",
    meta: {
      title: "综合查询",
      icon: SearchOutlined,
    },
    component: Search,
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
export { routes };
