const reverseString = require('./reverseString')

function hello() { 
    return "hello";
}

function isPalindrome(word) { 
    return word.toLowerCase() === reverseString(word).toLowerCase()
}

module.exports = isPalindrome