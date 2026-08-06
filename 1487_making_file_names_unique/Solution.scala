object Solution {
  def getFolderNames(names: Array[String]): Array[String] = {
    val used = scala.collection.mutable.HashMap.empty[String, Int]
    names.map { name =>
      val candidate = used.get(name) match {
        case None => name
        case Some(start) =>
          var suffix = start
          while (used.contains(s"$name($suffix)")) suffix += 1
          used(name) = suffix + 1
          s"$name($suffix)"
      }
      used(candidate) = 1
      candidate
    }
  }
}
