package org.maslov.graph.jgrapht.snippets;

import com.mxgraph.layout.mxCircleLayout;
import com.mxgraph.layout.mxIGraphLayout;
import com.mxgraph.util.mxCellRenderer;
import org.jgrapht.ext.JGraphXAdapter;
import org.jgrapht.graph.DefaultDirectedGraph;
import org.jgrapht.graph.DefaultEdge;

import javax.imageio.ImageIO;
import javax.imageio.ImageTypeSpecifier;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

public class GraphVisualisation {
    public static void main(String[] args) {
        File imgFile = new File("graph.png");
        try {
            imgFile.createNewFile();


            DefaultDirectedGraph<String, DefaultEdge> g =
                    new DefaultDirectedGraph<String, DefaultEdge>(DefaultEdge.class);

            String x1 = "x1";
            String x2 = "x2";
            String x3 = "x3";
            String x4 = "x4";
            String x5 = "x5";

            g.addVertex(x1);
            g.addVertex(x2);
            g.addVertex(x3);
            g.addVertex(x4);
            g.addVertex(x5);

            g.addEdge(x1, x2);
            g.addEdge(x2, x3);
            g.addEdge(x3, x4);
            g.addEdge(x4, x5);
            g.addEdge(x5, x1);

            JGraphXAdapter<String, DefaultEdge> graphAdapter =
                    new JGraphXAdapter<String, DefaultEdge>(g);
            mxIGraphLayout layout = new mxCircleLayout(graphAdapter);
            layout.execute(graphAdapter.getDefaultParent());


            BufferedImage image =
                    mxCellRenderer.createBufferedImage(graphAdapter, null, 2, Color.WHITE, true, null);
            ImageIO.write(image, "PNG", imgFile);

            //assertTrue(imgFile.exists());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

}
