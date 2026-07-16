// LeetCode 0332 - Reconstruct Itinerary

// https://leetcode.com/problems/reconstruct-itinerary/



import scala.collection.mutable



object Solution {

  def findItinerary(tickets: List[List[String]]): List[String] = {

    val targets = mutable.Map.empty[String, mutable.ListBuffer[String]]

    for (List(source, destination) <- tickets.sorted.reverse) {

      targets.getOrElseUpdate(source, mutable.ListBuffer.empty[String]) += destination

    }



    val route = mutable.ListBuffer.empty[String]

    visit("JFK", targets, route)

    route.reverse.toList

  }



  private def visit(

      airport: String,

      targets: mutable.Map[String, mutable.ListBuffer[String]],

      route: mutable.ListBuffer[String]

  ): Unit = {

    val destinations = targets.get(airport)

    if (destinations.isDefined) {

      while (destinations.get.nonEmpty) {

        visit(destinations.get.remove(destinations.get.length - 1), targets, route)

      }

    }

    route += airport

  }

}
