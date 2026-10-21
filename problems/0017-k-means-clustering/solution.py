def k_means_clustering(
    points: list[tuple[float, ...]],
    k: int,
    initial_centroids: list[tuple[float, ...]],
    max_iterations: int
) -> list[tuple[float, ...]]:

    centroids = [tuple(c) for c in initial_centroids]

    for _ in range(max_iterations):

        # Create k empty clusters
        clusters = [[] for _ in range(k)]

        # Assign each point to nearest centroid
        for point in points:

            distances = []

            for centroid in centroids:

                distance = sum(
                    (point[i] - centroid[i]) ** 2
                    for i in range(len(point))
                )

                distances.append(distance)

            nearest = distances.index(min(distances))

            clusters[nearest].append(point)

        # Calculate new centroids
        new_centroids = []

        for i in range(k):

            # If cluster is empty, keep old centroid
            if len(clusters[i]) == 0:
                new_centroids.append(centroids[i])

            else:
                dimension = len(points[0])

                new_centroid = tuple(
                    sum(point[j] for point in clusters[i])
                    / len(clusters[i])
                    for j in range(dimension)
                )

                new_centroids.append(new_centroid)

        # Stop if centroids don't change
        if new_centroids == centroids:
            break

        centroids = new_centroids

    # Round final centroids to 4 decimal places
    final_centroids = [
        tuple(round(value, 4) for value in centroid)
        for centroid in centroids
    ]

    return final_centroids