const colors = require('tailwindcss/colors')

module.exports = {
  theme: {
    extend: {
      colors: {
        // you can either spread `colors` to apply all the colors
        ...colors,
        // or add them one by one and name whatever you want
        amber: colors.amber,
        emerald: colors.emerald,
        rose: colors.rose,
      }
    }
  }
}