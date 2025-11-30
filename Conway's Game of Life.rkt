;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-lambda-reader.ss" "lang")((modname |Conway's Game of Life|) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #t)))
(define grid1 '((□ ■ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □)
                (□ □ ■ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □)
                (■ ■ ■ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □)
                (□ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □)
                (□ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □)
                (□ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □)
                (□ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □)
                (□ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □)
                (□ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □)
                (□ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □)
                (□ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □)
                (□ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □)
                (□ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □)
                (□ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □)
                (□ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □)
                (□ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □)
                (□ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □)
                (□ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □)
                (□ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □)
                (□ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □)
                (□ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □)
                (□ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □)
                (□ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □)
                (□ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □)
                (□ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □)))

(define grid2 '((□ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □)
                (□ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ ■ □ □ □ □ □ □ □ □ □ □ □ □)
                (□ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ ■ □ ■ □ □ □ □ □ □ □ □ □ □ □ □)
                (□ □ □ □ □ □ □ □ □ □ □ □ □ ■ ■ □ □ □ □ □ □ ■ ■ □ □ □ □ □ □ □ □ □ □ □ □ ■ ■ □)
                (□ □ □ □ □ □ □ □ □ □ □ □ ■ □ □ □ ■ □ □ □ □ ■ ■ □ □ □ □ □ □ □ □ □ □ □ □ ■ ■ □)
                (□ ■ ■ □ □ □ □ □ □ □ □ ■ □ □ □ □ □ ■ □ □ □ ■ ■ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □)
                (□ ■ ■ □ □ □ □ □ □ □ □ ■ □ □ □ ■ □ ■ ■ □ □ □ □ ■ □ ■ □ □ □ □ □ □ □ □ □ □ □ □)
                (□ □ □ □ □ □ □ □ □ □ □ ■ □ □ □ □ □ ■ □ □ □ □ □ □ □ ■ □ □ □ □ □ □ □ □ □ □ □ □)
                (□ □ □ □ □ □ □ □ □ □ □ □ ■ □ □ □ ■ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □)
                (□ □ □ □ □ □ □ □ □ □ □ □ □ ■ ■ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □)
                (□ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ ■ □ □ □ □ □ □ □ □ □ □ □ □ □)
                (□ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ ■ ■ □ □ □ □ □ □ □ □ □ □ □)
                (□ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ ■ ■ □ □ □ □ □ □ □ □ □ □ □ □)
                (□ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □)
                (□ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □)
                (□ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □)
                (□ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □)
                (□ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □)
                (□ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ ■ ■ □ □ □ □)
                (□ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ ■ □ ■ □ □ □)
                (□ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ ■ □ □ □)
                (□ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ ■ ■ □ □)
                (□ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □)))

(define (alive? cell)
  (cond
    [(symbol=? '■ cell) 1]
    [else 0]))

(define (update-cell old col row width height)
  (local [(define cell (list-ref (list-ref old row) col))
          (define neighbours (+ (alive? (list-ref (list-ref old (modulo (add1 row) height))
                                                  col))
                                (alive? (list-ref (list-ref old (modulo (add1 row) height))
                                                  (modulo (add1 col) width)))
                                (alive? (list-ref (list-ref old row)
                                                  (modulo (add1 col) width)))
                                (alive? (list-ref (list-ref old (modulo (sub1 row) height))
                                                  (modulo (add1 col) width)))
                                (alive? (list-ref (list-ref old (modulo (sub1 row) height))
                                                  col))
                                (alive? (list-ref (list-ref old (modulo (sub1 row) height))
                                                  (modulo (sub1 col) width)))
                                (alive? (list-ref (list-ref old row)
                                                  (modulo (sub1 col) width)))
                                (alive? (list-ref (list-ref old (modulo (add1 row) height))
                                                  (modulo (sub1 col) width)))))]
    (cond
      [(= 3 neighbours) '■]
      [(= 2 neighbours) cell]
      [else '□])))

(define (next-gen/acc old new col row width height)
  (cond
    [(zero? row) (rest new)]
    [(zero? col) (next-gen/acc old (cons empty new)
                               width (sub1 row) width  height)]
    [else (next-gen/acc old (cons (cons (update-cell old (sub1 col) (sub1 row) width height)
                                        (first new)) (rest new))
                        (sub1 col) row width height)]))

(define (conway/acc log n width height)
  (cond
    [(zero? n) log]
    [else (conway/acc (cons (next-gen/acc (first log) (list empty)
                                          width height width height) log)
                      (sub1 n) width height)]))

(define (Conway grid n)
  (reverse (conway/acc (list grid) n (length (first grid)) (length grid))))

(Conway grid2 756); (Drag bottom window to top.)