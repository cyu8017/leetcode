// LeetCode 2694 - Event Emitter
// https://leetcode.com/problems/event-emitter/

import scala.collection.mutable

class EventEmitter() {
  private val handlers = mutable.HashMap.empty[String, mutable.ArrayBuffer[Array[Int] => Unit]]

  def subscribe(eventName: String, callback: Array[Int] => Unit): () => Unit = {
    val list = handlers.getOrElseUpdate(eventName, mutable.ArrayBuffer.empty[Array[Int] => Unit])
    list += callback
    var idx = list.length - 1
    () => {
      val v = handlers.get(eventName)
      if (v.isDefined && idx >= 0 && idx < v.get.length) {
        v.get.remove(idx)
        idx = -1
      }
    }
  }

  def emit(eventName: String, args: Array[Int]): Array[Int] = {
    val res = mutable.ArrayBuffer.empty[Int]
    handlers.get(eventName).foreach { list =>
      list.toList.foreach { cb =>
        cb(args)
        res += 0
      }
    }
    res.toArray
  }
}

object Solution {
  def createEmitter(): EventEmitter = new EventEmitter()
}
