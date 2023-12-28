/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./portfolioProject/core/templates/core/*.html'],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui")],
  daisyui: {
    themes:["lofi"],
  }
}

