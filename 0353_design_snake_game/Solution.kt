// LeetCode 0353 - Design Snake Game

// https://leetcode.com/problems/design-snake-game/



class SnakeGame(

    private val width: Int,

    private val height: Int,

    private val food: Array<IntArray>,

) {

    private var foodIndex = 0

    private var score = 0

    private val snake = ArrayDeque<IntArray>()

    private val body = mutableSetOf<String>()



    init {

        snake.addFirst(intArrayOf(0, 0))

        body.add("0,0")

    }



    fun move(direction: String): Int {

        val head = snake.first()

        var row = head[0]

        var col = head[1]



        when (direction) {

            "U" -> row--

            "D" -> row++

            "L" -> col--

            else -> col++

        }



        if (row < 0 || row >= height || col < 0 || col >= width) {

            return -1

        }



        val willEat = foodIndex < food.size

            && row == food[foodIndex][0]

            && col == food[foodIndex][1]



        if (!willEat) {

            val tail = snake.removeLast()

            body.remove("${tail[0]},${tail[1]}")

        }



        val key = "$row,$col"

        if (key in body) {

            return -1

        }



        snake.addFirst(intArrayOf(row, col))

        body.add(key)



        if (willEat) {

            score++

            foodIndex++

        }



        return score

    }

}
