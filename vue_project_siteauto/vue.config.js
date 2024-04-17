const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  filenameHashing: false,
  publicPath: '/static/',
  assetsDir: 'static_vue'
})
