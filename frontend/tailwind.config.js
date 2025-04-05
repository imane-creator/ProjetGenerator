/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './static/js/**/*.js',
    // Ajoutez tous les chemins qui contiennent des fichiers où des classes CSS sont utilisées
  ],
  safelist: [
    'group-hover:opacity-100', // Ajoutez ici toutes les classes que vous souhaitez garder
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

