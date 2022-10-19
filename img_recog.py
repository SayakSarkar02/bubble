image = cv2.imread("Assets/cards.jpg")

width, height = 250, 350
point1 = np.float32([[111, 219], [287, 188], [154, 482], [352, 440]])
point2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(point1, point2)
Output = cv2.warpPerspective(image, matrix, (width, height))

cv2.imshow("Image”, image)
    cv2.imshow("Output”, Output)
      cv2.waitKey(0)
