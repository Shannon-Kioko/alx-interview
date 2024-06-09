process.env.NODE_TLS_REJECT_UNAUTHORIZED = '0';
async function getStarWarsCharacters() {

    // try {
    const response = await fetch(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`)
    console.log(response);
}

// Your code here
// catch (error) {
//         if (error.code === 'ECONNRESET') {
//             console.error('Connection reset by peer');
//         } else {
//             throw error;
//         }
//     }

getStarWarsCharacters(); // This should print the response object
