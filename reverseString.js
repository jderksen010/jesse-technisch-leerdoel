function reverseString(word) { 
    return word.toLowerCase().split('')
        .reverse().join('').replaceAll(',', '')
}

module.exports = reverseString;