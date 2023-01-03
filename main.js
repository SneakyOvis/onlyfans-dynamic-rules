import { readdirSync, writeFileSync } from 'fs';

writeFileSync('test.txt', 'test');
const files = readdirSync('.');
console.log(files);
