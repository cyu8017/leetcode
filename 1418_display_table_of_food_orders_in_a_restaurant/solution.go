// LeetCode 1418 - Display Table of Food Orders in a Restaurant
// https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/

import (
	"sort"
	"strconv"
)

func displayTable(orders [][]string) [][]string {
	foodSet := map[string]bool{}
	tableSet := map[int]bool{}
	counts := map[[2]interface{}]int{}
	type key struct {
		table int
		food  string
	}
	counts2 := map[key]int{}
	for _, o := range orders {
		table, _ := strconv.Atoi(o[1])
		food := o[2]
		foodSet[food] = true
		tableSet[table] = true
		counts2[key{table, food}]++
	}
	_ = counts
	foods := make([]string, 0, len(foodSet))
	for f := range foodSet {
		foods = append(foods, f)
	}
	sort.Strings(foods)
	tables := make([]int, 0, len(tableSet))
	for t := range tableSet {
		tables = append(tables, t)
	}
	sort.Ints(tables)
	result := [][]string{append([]string{"Table"}, foods...)}
	for _, table := range tables {
		row := []string{strconv.Itoa(table)}
		for _, food := range foods {
			row = append(row, strconv.Itoa(counts2[key{table, food}]))
		}
		result = append(result, row)
	}
	return result
}
