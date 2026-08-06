object Solution {
  def findMinFibonacciNumbers(k: Int): Int = { val f=scala.collection.mutable.ArrayBuffer(1,1); while(f.last<k)f += f(f.length-1)+f(f.length-2); var rem=k; var ans=0; f.reverseIterator.foreach(x => if(x<=rem){rem-=x;ans+=1}); ans }
}
