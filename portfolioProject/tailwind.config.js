/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./core/templates/core/*.html'],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui")],
  daisyui: {
    themes:["lofi"],
  }
}

