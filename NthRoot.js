const perfectRoots = (n) => [1/2, 1/4, 1/8].map(el=> Math.pow(n, el) % 1 === 0 ).every(e => e === true)