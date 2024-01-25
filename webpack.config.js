const path = require('path');

module.exports = {
  mode: 'production',
  entry: './assets/index.js',
  output: {
    path: path.resolve(__dirname, 'static'),
    filename: 'bundle.js',
  },
  module: {
    rules: [
      {
        test: /\.js$/i,
        include: path.resolve(__dirname, 'assets'),
        // use: {
          // loader: 'babel-loader',
          // options: {
            // presets: ['@babel/preset-env'],
          // },
        // },
      },
      {
        test: /\.css$/i,
        include: path.resolve(__dirname, 'assets'),
        use: ['style-loader', 'css-loader', 'postcss-loader'],
      },
    ],
  },
  devServer: {
    static: 'static',
    // watchFiles: true,
  },
};