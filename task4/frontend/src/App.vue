<script setup>
import { routes } from "./router.js";
</script>

<template>
  <div class="flex flex-row h-full">
    <div class="flex flex-col w-1/6 py-2 bg-gray-100 select-none shadow-xl">
      <router-link v-for="route in routes" :key="route.path" :to="route.path" class="menu-item-container"
        v-slot="{ isActive }">
        <div class="menu-item" :class="{ 'item-selected': isActive }">
          <n-icon size="1.5em" :component="route.meta?.icon" />
          <span class="ml-3">{{ route.meta?.title }}</span>
        </div>
      </router-link>
    </div>
    <div class="w-5/6 px-6 pt-2 pb-4 flex flex-col">
      <router-view v-slot="{ Component }">
        <keep-alive>
          <component :is="Component" />
        </keep-alive>
      </router-view>
    </div>
  </div>
</template>

<style scoped>
.menu-item-container {
  @apply py-2;
}

.menu-item-container:hover {
  @apply bg-gray-200;
}

.menu-item {
  @apply px-2 flex flex-row items-center box-content border-l-4 border-l-blue-600 border-opacity-0;
}

.item-selected {
  @apply border-opacity-100;
}
</style>
