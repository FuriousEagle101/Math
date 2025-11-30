;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-lambda-reader.ss" "lang")((modname fractran) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #t)))
(define-struct frac (num den))

(define program (list (make-frac 17 91)
                      (make-frac 78 85)
                      (make-frac 19 51)
                      (make-frac 23 38)
                      (make-frac 29 33)
                      (make-frac 77 29)
                      (make-frac 95 23)
                      (make-frac 77 19)
                      (make-frac 1 17)
                      (make-frac 11 13)
                      (make-frac 13 11)
                      (make-frac 15 2)
                      (make-frac 1 7)
                      (make-frac 55 1)))

(define (next n frac-lst)
  (cond
    [(= (modulo n (frac-den (first frac-lst))) 0)
     (* n (/ (frac-num (first frac-lst))
             (frac-den (first frac-lst))))]
    [else (next n (rest frac-lst))]))

(define (apply-program n prog acc)
  (local [(define nf (next n prog))]
    (cond
      [(zero? acc) empty]
      [else (cons nf (apply-program nf prog (sub1 acc)))])))

(define (log-2 x acc)
  (cond
    [(= (modulo x 2) 0) (log-2 (/ x 2) (add1 acc))]
    [(= x 1) acc]
    [else false]))

(define (primes N)
  (local [(define sequence (cons 2 (apply-program 2 program N)))
          (define prime-lst (foldr (lambda (x rror)
                                     (local [(define log2x (log-2 x 0))]
                                       (cond
                                         [(false? log2x) rror]
                                         [else (cons log2x rror)]))) empty sequence))]
    (rest prime-lst)))

(primes 1000000)