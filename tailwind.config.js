// tailwind.config.js
export default {
  content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        u: {
          bg: "#dbeafe", // blue-100
          text: "#1e40af", // blue-800
        },
        v: {
          bg: "#ffedd5", // orange-100
          text: "#9a3412", // orange-800
        },
        w: {
          bg: "#e5e7eb", // gray-200
          text: "#1f2937", // gray-800
        },
      },
    },
  },
  plugins: [],
};
