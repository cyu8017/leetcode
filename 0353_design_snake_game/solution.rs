// LeetCode 0353 - Design Snake Game
// https://leetcode.com/problems/design-snake-game/

use std::collections::{HashSet, VecDeque};

struct SnakeGame {
    width: i32,
    height: i32,
    food: Vec<Vec<i32>>,
    food_index: usize,
    score: i32,
    snake: VecDeque<(i32, i32)>,
    body: HashSet<(i32, i32)>,
}

impl SnakeGame {
    fn new(width: i32, height: i32, food: Vec<Vec<i32>>) -> Self {
        let mut snake = VecDeque::new();
        snake.push_back((0, 0));
        let mut body = HashSet::new();
        body.insert((0, 0));

        Self {
            width,
            height,
            food,
            food_index: 0,
            score: 0,
            snake,
            body,
        }
    }

    fn mov(&mut self, direction: String) -> i32 {
        let (mut row, mut col) = *self.snake.front().unwrap();

        match direction.as_str() {
            "U" => row -= 1,
            "D" => row += 1,
            "L" => col -= 1,
            _ => col += 1,
        }

        if row < 0 || row >= self.height || col < 0 || col >= self.width {
            return -1;
        }

        let will_eat = self.food_index < self.food.len()
            && row == self.food[self.food_index][0]
            && col == self.food[self.food_index][1];

        if !will_eat {
            if let Some(tail) = self.snake.pop_back() {
                self.body.remove(&tail);
            }
        }

        let head = (row, col);
        if self.body.contains(&head) {
            return -1;
        }

        self.snake.push_front(head);
        self.body.insert(head);

        if will_eat {
            self.score += 1;
            self.food_index += 1;
        }

        self.score
    }
}
