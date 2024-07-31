module.exports = {
    content: ["./src/**/*.{astro,html,svelte,vue,js,ts,jsx,tsx}"],
    plugins: [require("daisyui")],
    daisyui: {
        themes: ["light", "dark", "sunset"],
    },
};
