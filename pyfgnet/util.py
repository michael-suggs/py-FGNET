def plot_svc(svc, X, Y, h=.02, pad=.25):
    x_min, x_max = X.iloc[:, 0].min() - pad, X.iloc[:, 0].max() + pad
    y_min, y_max = X.iloc[:, 1].min() - pad, X.iloc[:, 1].max() + pad
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    Z = svc.predict()
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, cmap=plt.cm.Paired, alpha=.2)
