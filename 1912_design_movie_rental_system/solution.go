// LeetCode 1912 - Design Movie Rental System
// https://leetcode.com/problems/design-movie-rental-system/

import "sort"

type MovieRentingSystem struct {
	price     map[[2]int]int
	available map[int][][2]int // movie -> (price, shop)
	rented    [][3]int         // (price, shop, movie)
}

func Constructor(n int, entries [][]int) MovieRentingSystem {
	m := MovieRentingSystem{
		price:     make(map[[2]int]int),
		available: make(map[int][][2]int),
	}
	for _, e := range entries {
		shop, movie, price := e[0], e[1], e[2]
		m.price[[2]int{shop, movie}] = price
		arr := m.available[movie]
		arr = append(arr, [2]int{price, shop})
		sort.Slice(arr, func(i, j int) bool {
			if arr[i][0] != arr[j][0] {
				return arr[i][0] < arr[j][0]
			}
			return arr[i][1] < arr[j][1]
		})
		m.available[movie] = arr
	}
	return m
}

func (this *MovieRentingSystem) Search(movie int) []int {
	arr := this.available[movie]
	limit := 5
	if len(arr) < limit {
		limit = len(arr)
	}
	res := make([]int, limit)
	for i := 0; i < limit; i++ {
		res[i] = arr[i][1]
	}
	return res
}

func (this *MovieRentingSystem) Rent(shop int, movie int) {
	price := this.price[[2]int{shop, movie}]
	arr := this.available[movie]
	for i, v := range arr {
		if v[0] == price && v[1] == shop {
			this.available[movie] = append(arr[:i], arr[i+1:]...)
			break
		}
	}
	this.rented = append(this.rented, [3]int{price, shop, movie})
	sort.Slice(this.rented, func(i, j int) bool {
		a, b := this.rented[i], this.rented[j]
		if a[0] != b[0] {
			return a[0] < b[0]
		}
		if a[1] != b[1] {
			return a[1] < b[1]
		}
		return a[2] < b[2]
	})
}

func (this *MovieRentingSystem) Drop(shop int, movie int) {
	price := this.price[[2]int{shop, movie}]
	for i, v := range this.rented {
		if v[0] == price && v[1] == shop && v[2] == movie {
			this.rented = append(this.rented[:i], this.rented[i+1:]...)
			break
		}
	}
	arr := this.available[movie]
	arr = append(arr, [2]int{price, shop})
	sort.Slice(arr, func(i, j int) bool {
		if arr[i][0] != arr[j][0] {
			return arr[i][0] < arr[j][0]
		}
		return arr[i][1] < arr[j][1]
	})
	this.available[movie] = arr
}

func (this *MovieRentingSystem) Report() [][]int {
	limit := 5
	if len(this.rented) < limit {
		limit = len(this.rented)
	}
	res := make([][]int, limit)
	for i := 0; i < limit; i++ {
		res[i] = []int{this.rented[i][1], this.rented[i][2]}
	}
	return res
}
