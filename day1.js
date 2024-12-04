// https://adventofcode.com/2024/day/1

function parse1 (inputString) {
    const lines = inputString.trim().split("\n");
    const arr1 = [];
    const arr2 = [];
    for (let line of lines) {
        const [n1, n2] = line.trim().split(/\s+/).map(Number);
        arr1.push(n1);
        arr2.push(n2);
    }
    return [arr1, arr2];
}

function day1Solution1 (input) {
    input = parse1 (input);
    const arr1 = input[0].sort();
    const arr2 = input[1].sort();
    let res = 0;
    for (let i=0; i<arr1.length; i++) {
        res += Math.abs((arr1[i]-arr2[i]));
    }
    return res;
}
console.log("Answer 1: 3714264")

function day1Solution2 (input) {
    const [left, right] = parse1(input);
    const rightCount = {};
    for (let n of right) {
        rightCount[n] = (rightCount[n] || 0) + 1;
    };
    let similarityScore = 0
    for (let n of left) {
        const count = rightCount[n] || 0
        similarityScore += n * count
    }
    return similarityScore
}

console.log("Answer 2: 18805872")

