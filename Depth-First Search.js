//island 문제

const input = [
  ["1", "1", "1", "1", "1"],
  ["1", "1", "1", "1", "0"],
  ["1", "1", "0", "0", "0"],
  ["0", "0", "1", "1", "0"],
  ["0", "0", "0", "0", "0"],
  ["0", "1", "0", "0", "0"],
  ["0", "0", "0", "1", "1"],
  ["1", "0", "0", "1", "1"],
  ["1", "0", "0", "0", "0"],
  ["1", "1", "0", "0", "0"],
];

function main(grid) {
  // N x M matrix
  let numOfIsland = 0;
  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[0].length; j++) {
      if (grid[i][j] === "1") {
        dfs(grid, i, j);
        numOfIsland++;
        console.log(grid);
      }
    }
  }

  console.log(numOfIsland);
}

// recursion
function dfs(grid, i, j) {
  // end clause
  if (
    i < 0 ||
    i >= grid.length ||
    j < 0 ||
    j >= grid[0].length ||
    grid[i][j] === "0"
  )
    return;

  grid[i][j] = "0";
  const direction = [
    [-1, 0],
    [0, 1],
    [1, 0],
    [0, -1],
  ];

  for (let d = 0; d < direction.length; d++) {
    const newI = direction[d][0] + i;
    const newJ = direction[d][1] + j;
    dfs(grid, newI, newJ);
  }
  return;
}

main(input);
