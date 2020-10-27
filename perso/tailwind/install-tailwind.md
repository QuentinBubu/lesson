# How to install Tailwind:
1. npm init -y
2. npx tailwind init
3. create `postcss.config.js` file
4. add modules:
```js
module.exports = {
    plugins: [
        require('tailwindcss'),
        require('autoprefixer'),
    ]
}
```
5. create `css/tailwind.css` file
6. add
```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```
7. into `package.json`, modify `"test": "..."` to `"build": "postcss css/tailwind.css -o public/build/tailwind.css"`
8. (npm uninstall postcss)
9. (npm i postcss)
10. npm run build 