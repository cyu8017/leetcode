object Solution {
  def longestDiverseString(a: Int, b: Int, c: Int): String = { val q=scala.collection.mutable.PriorityQueue[(Int,Char)]()(Ordering.by(_._1)); if(a>0)q.enqueue((a,'a')); if(b>0)q.enqueue((b,'b')); if(c>0)q.enqueue((c,'c')); val out=new StringBuilder; while(q.nonEmpty) { val cur=q.dequeue(); if(out.length>=2 && out.takeRight(2).forall(_==cur._2)) { if(q.isEmpty) return out.toString; val nxt=q.dequeue(); out += nxt._2; if(nxt._1>1)q.enqueue((nxt._1-1,nxt._2)); q.enqueue(cur) } else { out += cur._2; if(cur._1>1)q.enqueue((cur._1-1,cur._2)) } }; out.toString }
}
