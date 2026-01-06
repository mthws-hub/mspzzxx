import ec.edu.espe.repasoprueba.view.FrmView;
import javax.swing.SwingUtilities;

/**
 *
 * @author Mathews Pastor, The POOwer Rangers Of Programming
 */
public class Main {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            new FrmView().setVisible(true);
        });
    }
}
