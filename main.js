import { readdirSync, writeFileSync } from 'fs';

writeFileSync('test.txt', Math.random().toString());
