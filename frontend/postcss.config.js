import tailwindcss from '@tailwindcss/postcss'; // Correct import for v4 plugin
import autoprefixer from 'autoprefixer';      // Make sure autoprefixer is also imported

export default {
  plugins: [ // Change from an object to an array
    tailwindcss(), // Call the function to get the plugin instance
    autoprefixer   // Include autoprefixer directly (it's not a factory function)
  ],
};