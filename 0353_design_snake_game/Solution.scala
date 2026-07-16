// LeetCode 0353 - Design Snake Game

// https://leetcode.com/problems/design-snake-game/



import scala.collection.mutable



class SnakeGame(width: Int, height: Int, food: Array[Array[Int]]) {

  private var foodIndex = 0

  private var score = 0

  private val snake = mutable.ArrayDeque(Array(0, 0))

  private val body = mutable.Set("0,0")



  def move(direction: String): Int = {

    val head = snake.head

    var row = head(0)

    var col = head(1)



    direction match {

      case "U" => row -= 1

      case "D" => row += 1

      case "L" => col -= 1

      case _ => col += 1

    }



    if (row < 0 || row >= height || col < 0 || col >= width) {

      -1

    } else {

      val willEat = foodIndex < food.length

        && row == food(foodIndex)(0)

        && col == food(foodIndex)(1)



      if (!willEat) {

        val tail = snake.removeLast()

        body.remove(s"${tail(0)},${tail(1)}")

      }



      val key = s"$row,$col"

      if (body.contains(key)) {

        -1

      } else {

        snake.prepend(Array(row, col))

        body += key



        if (willEat) {

          score += 1

          foodIndex += 1

        }



        score

      }

    }

  }

}
