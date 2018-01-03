# TSP-by-Ant-Colony-Optimization
solve the TSP-52 problem by ACO  
  
language: python(without pypy)  

**main method**: by random-proportional rule  
more about random-proportional rule, see http://www-igm.univ-mlv.fr/~lombardy/ens/JavaTTT0708/fourmis.pdf  
  
**benchline**: without heuristic parameter η(inverse of distance, see random-proportional rule)  
  
performance:  
52 points tsp  

    main method:  
        about 2.5 seconds time used  
        7544.662211251633 best result(in 50 test) (global best 7544.365901904086)  
    benchline:  
        about 23-25 seconds time used  
        20909.14393444202 best result (in 10 test)  
        
130 points tsp  

    main method:  
        about 40 seconds time used  
        6518.212887978163 best result (in 20 test)  
    ~~benchline:~~  
