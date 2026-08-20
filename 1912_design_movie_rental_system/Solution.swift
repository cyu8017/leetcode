// LeetCode 1912 - Design Movie Rental System
// https://leetcode.com/problems/design-movie-rental-system/

class MovieRentingSystem {
    private var price: [Int64: Int] = [:]
    private var available: [Int: [(Int, Int)]] = [:] // movie -> [(price, shop)]
    private var rented: [(Int, Int, Int)] = [] // (price, shop, movie)

    init(_ n: Int, _ entries: [[Int]]) {
        for e in entries {
            let shop = e[0], movie = e[1], p = e[2]
            price[key(shop, movie)] = p
            insertAvail(movie, p, shop)
        }
    }

    private func key(_ shop: Int, _ movie: Int) -> Int64 {
        Int64(shop) << 32 | Int64(movie)
    }

    private func insertAvail(_ movie: Int, _ p: Int, _ shop: Int) {
        var arr = available[movie] ?? []
        let item = (p, shop)
        var lo = 0, hi = arr.count
        while lo < hi {
            let mid = (lo + hi) / 2
            if arr[mid].0 < p || (arr[mid].0 == p && arr[mid].1 < shop) {
                lo = mid + 1
            } else {
                hi = mid
            }
        }
        arr.insert(item, at: lo)
        available[movie] = arr
    }

    private func removeAvail(_ movie: Int, _ p: Int, _ shop: Int) {
        guard var arr = available[movie] else { return }
        if let idx = arr.firstIndex(where: { $0.0 == p && $0.1 == shop }) {
            arr.remove(at: idx)
            available[movie] = arr
        }
    }

    private func insertRented(_ p: Int, _ shop: Int, _ movie: Int) {
        let item = (p, shop, movie)
        var lo = 0, hi = rented.count
        while lo < hi {
            let mid = (lo + hi) / 2
            let cur = rented[mid]
            if cur.0 < p || (cur.0 == p && cur.1 < shop) || (cur.0 == p && cur.1 == shop && cur.2 < movie) {
                lo = mid + 1
            } else {
                hi = mid
            }
        }
        rented.insert(item, at: lo)
    }

    private func removeRented(_ p: Int, _ shop: Int, _ movie: Int) {
        if let idx = rented.firstIndex(where: { $0.0 == p && $0.1 == shop && $0.2 == movie }) {
            rented.remove(at: idx)
        }
    }

    func search(_ movie: Int) -> [Int] {
        Array((available[movie] ?? []).prefix(5).map { $0.1 })
    }

    func rent(_ shop: Int, _ movie: Int) {
        let p = price[key(shop, movie)]!
        removeAvail(movie, p, shop)
        insertRented(p, shop, movie)
    }

    func drop(_ shop: Int, _ movie: Int) {
        let p = price[key(shop, movie)]!
        removeRented(p, shop, movie)
        insertAvail(movie, p, shop)
    }

    func report() -> [[Int]] {
        Array(rented.prefix(5).map { [$0.1, $0.2] })
    }
}
