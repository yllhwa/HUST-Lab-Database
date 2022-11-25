import { createRouter, createWebHashHistory } from "vue-router";
import Index from "./pages/Index.vue";
import Students from "./pages/Students.vue";
import Courses from "./pages/Courses.vue";
import Grades from "./pages/Grades.vue";

import {
  HomeOutlined,
  PeopleAltOutlined,
  LibraryBooksOutlined,
  AutoAwesomeOutlined,
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
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
export { routes };
