% Facts about planets
planet(mercury).
planet(venus).
planet(earth).
planet(mars).
planet(jupiter).
planet(saturn).
planet(uranus).
planet(neptune).

% Facts about some properties of planets
size(mercury, small).
size(venus, small).
size(earth, medium).
size(mars, small).
size(jupiter, large).
size(saturn, large).
size(uranus, medium).
size(neptune, medium).

distance(mercury, sun, close).
distance(venus, sun, close).
distance(earth, sun, moderate).
distance(mars, sun, moderate).
distance(jupiter, sun, far).
distance(saturn, sun, far).
distance(uranus, sun, distant).
distance(neptune, sun, distant).

% Rules for querying the database
small_planet(X) :- planet(X), size(X, small).
large_planet(X) :- planet(X), size(X, large).

distance_from_sun(X, D) :- planet(X), distance(X, sun, D).
