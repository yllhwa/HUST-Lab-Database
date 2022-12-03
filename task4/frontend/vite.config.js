import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import Components from "unplugin-vue-components/vite";
import { NaiveUiResolver } from "unplugin-vue-components/resolvers";
import { viteSingleFile } from "vite-plugin-singlefile";

export default defineConfig({
  plugins: [
    vue({
      reactivityTransform: true,
    }),
    Components({
      resolvers: [NaiveUiResolver()],
    }),
    viteSingleFile(),
  ],
  define: {
    __VUE_OPTIONS_API__: false,
  },
  server: {
    proxy: {
      "/api": {
        target: "http://127.0.0.1:9999",
        changeOrigin: true,
      },
    },
  },
});
