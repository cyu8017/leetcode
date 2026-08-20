// LeetCode 2353 - Design a Food Rating System
// https://leetcode.com/problems/design-a-food-rating-system/

import "container/heap"

type item struct {
	food   string
	rating int
}

type FoodHeap []item

func (h FoodHeap) Len() int { return len(h) }
func (h FoodHeap) Less(i, j int) bool {
	if h[i].rating == h[j].rating {
		return h[i].food < h[j].food
	}
	return h[i].rating > h[j].rating
}
func (h FoodHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *FoodHeap) Push(x interface{}) { *h = append(*h, x.(item)) }
func (h *FoodHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

type FoodRatings struct {
	cuisineOf map[string]string
	ratingOf  map[string]int
	heaps     map[string]*FoodHeap
}

func Constructor(foods []string, cuisines []string, ratings []int) FoodRatings {
	fr := FoodRatings{
		cuisineOf: map[string]string{},
		ratingOf:  map[string]int{},
		heaps:     map[string]*FoodHeap{},
	}
	for i, food := range foods {
		fr.cuisineOf[food] = cuisines[i]
		fr.ratingOf[food] = ratings[i]
		if fr.heaps[cuisines[i]] == nil {
			h := &FoodHeap{}
			heap.Init(h)
			fr.heaps[cuisines[i]] = h
		}
		heap.Push(fr.heaps[cuisines[i]], item{food, ratings[i]})
	}
	return fr
}

func (this *FoodRatings) ChangeRating(food string, newRating int) {
	this.ratingOf[food] = newRating
	heap.Push(this.heaps[this.cuisineOf[food]], item{food, newRating})
}

func (this *FoodRatings) HighestRated(cuisine string) string {
	h := this.heaps[cuisine]
	for {
		top := (*h)[0]
		if this.ratingOf[top.food] == top.rating {
			return top.food
		}
		heap.Pop(h)
	}
}
