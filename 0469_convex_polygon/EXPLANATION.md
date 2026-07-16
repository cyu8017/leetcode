# How We Solve Convex Polygon

All turns around the polygon must bend in the same rotational direction.

## Steps

1. Walk consecutive triples of vertices (with wrap-around).
2. Compute the 2D cross product of edge vectors.
3. Require all non-zero cross products to share the same sign.
