import cv2
import numpy as np
import preprocess_img
import load_model

import tensorflow as tf

def grad_cam(array):
    img = preprocess_img.preprocess(array)
    model = load_model.model()
    grad_model = tf.keras.models.Model(
        model.inputs, [model.get_layer("conv10_thisone").output, model.output]
    )

    with tf.GradientTape() as tape:
        last_conv_layer_output, preds = grad_model([img])
        if isinstance(preds, list):
            preds = preds[0]
        pred_index = tf.argmax(preds[0])
        class_channel = preds[:, pred_index]
    
    grads = tape.gradient(class_channel, last_conv_layer_output)
    
    pooled_grads = tf.reduce_mean(grads, axis=(0, 1, 2))
    
    last_conv_layer_output = last_conv_layer_output[0]
    heatmap = last_conv_layer_output @ pooled_grads[..., tf.newaxis]
    heatmap = tf.squeeze(heatmap)
    
    heatmap = tf.maximum(heatmap, 0) / (tf.math.reduce_max(heatmap) + 1e-9)
    heatmap = heatmap.numpy()
    heatmap = cv2.resize(heatmap, (512, 512))
    heatmap = np.uint8(255 * heatmap)
    heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)
    img2 = cv2.resize(array, (512, 512))
    hif = 0.8
    transparency = heatmap * hif
    transparency = transparency.astype(np.uint8)
    superimposed_img = cv2.add(transparency, img2)
    superimposed_img = superimposed_img.astype(np.uint8)
    return superimposed_img[:, :, ::-1]