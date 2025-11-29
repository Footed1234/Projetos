import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.Graphics2D;

import javax.swing.JPanel;

public class GamePanel extends JPanel implements Runnable {
    // Configurações da tela
    final int originalTileSize = 16; // 16x16 tiles
    final int scale = 3;

    final int tileSize = originalTileSize * scale; // 48x48 tiles
    final int maxScreenCol = 16; // 16 colunas
    final int maxScreenRow = 12; // 12 linhas
    
    final int screenWidth = tileSize * maxScreenCol; // 768 pixels
    final int screenHeight = tileSize * maxScreenRow; // 576 pixels

    int FPS = 60;

    KeyHandler keyH = new KeyHandler();
    Thread gameThread;

    int playerx = 100;
    int playery = 100;
    int playerSpeed = 4;

    public GamePanel() {
        this.setPreferredSize(new Dimension(screenWidth, screenHeight));
        this.setBackground(Color.black);
        this.setDoubleBuffered(true);
        this.addKeyListener(keyH);
        this.setFocusable(true);
    }

    public void startGameThread() {
        gameThread = new Thread(this);
        gameThread.start();
    }

    //@Override
    // Sleep Method
    // public void run() {

    //     double drawInterval = 1000000000 / FPS; // 1 segundo em nanossegundos
    //     double nextDrawTime = System.nanoTime() + drawInterval;
        
    //     while (gameThread != null) {
    //         update();
    //         repaint();
            
    //         try {
    //             double remainingTime = nextDrawTime - System.nanoTime();
    //             remainingTime /= 1000000; // converte para milissegundos
                
    //             if (remainingTime < 0) {
    //                 remainingTime = 0;
    //             }

    //             Thread.sleep((long) remainingTime);
    //             nextDrawTime += drawInterval; // atualiza o próximo tempo de desenho
    //         } 
    //         catch (InterruptedException e) {
    //             e.printStackTrace();
    //         }
    //     }
    // }

    // Delta Time Method
    @Override
    public void run() {
        double drawInterval = 1000000000 / FPS; // 1 segundo em nanossegundos
        double delta = 0;
        long lastTime = System.nanoTime();
        long currentTime;
        long timer = 0;
        int drawCount = 0;

        while (gameThread != null) {
            currentTime = System.nanoTime();
            delta += (currentTime - lastTime) / drawInterval;
            timer += (currentTime - lastTime);
            lastTime = currentTime;

            if (delta >= 1) {
                update();
                repaint();
                delta--;
                drawCount++;
            }
            if (timer >= 1000000000) { // 1 segundo em nanossegundos
                System.out.println("FPS: " + drawCount);
                drawCount = 0;
                timer = 0;
            }
        }
    }

    public void update() {
        if (keyH.upPressed == true) {
            playery -= playerSpeed;
        }
        if (keyH.downPressed == true) {
            playery += playerSpeed;
        }
        if (keyH.leftPressed == true) {
            playerx -= playerSpeed;
        }
        if (keyH.rightPressed == true) {
            playerx += playerSpeed;
        }
    }

    public void paintComponent(Graphics g) {
        super.paintComponent(g);
        Graphics2D g2 = (Graphics2D) g;  
        g2.setColor(Color.white);
        g2.fillRect(playerx, playery, tileSize, tileSize);
        g2.dispose();
    }
}
