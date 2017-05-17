/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package quotation;

import java.awt.BorderLayout;

import javax.swing.JFrame;  
import javax.swing.JLabel;  
import javax.swing.JPasswordField;  
import javax.swing.JTextArea; 
import javax.swing.JButton;
import javax.swing.JTextField;  
import javax.swing.JPanel;  
import javax.swing.event.CaretEvent;  
import javax.swing.event.CaretListener; 
import java.awt.*;
import javax.swing.*;
/**
 *
 * @author lenovo
 */
public class Quotation extends JFrame {

    /**
     * @param args the command line arguments
     */
    
    public static void main(String[] args) {
        // TODO code application logic here
        Quotation tt = new Quotation();  
        tt.setVisible(true);  
    }
    
    private JLabel label = new JLabel("Status");  
 
    private JTextField textField;  
 
    private JPasswordField pwdField;  
 
    private JTextArea textArea;  
 
    public Quotation() {  
        super("股票行情");  
        setSize(700,700);
        setLocation(30,50);
        setVisible(true);
        setDefaultCloseOperation(EXIT_ON_CLOSE);  
        getContentPane().setLayout(new java.awt.FlowLayout());  
 
        textField = new JTextField(15);  
        JPanel panel = new JPanel();  
        JButton button =new JButton("搜索");
        panel.add(button);   
 
        /* 监听文本光标移动事件 */ 
        textField.addCaretListener(new CaretListener() {  
            public void caretUpdate(CaretEvent e) {  
                // 如果改变了内容，就可以即时更新 label 显示的内容  
                label.setText(textField.getText());  
            }  
        });  
 
;  
 
        textArea = new JTextArea(44, 45);  
        textArea.setLineWrap(true);  
 
        getContentPane().add(textField); 
        getContentPane().add(panel, BorderLayout.NORTH); 
        getContentPane().add(label);
        //getContentPane().add(textArea);  
        //SimpleTableTest stt= new SimpleTableTest();
        //getContentPane().add(stt);
        new SimpleTable().init();  
 
         
    } 
    
    public class SimpleTable  
{  
    JFrame jf = new JFrame("简单表格");  
    JTable table;  
    //定义二维数组作为表格数据  
    Object[][] tableData =   
    {  
        new Object[]{"李清照" , 29 , "女"},  
        new Object[]{"苏格拉底", 56 , "男"},  
        new Object[]{"李白", 35 , "男"},  
        new Object[]{"弄玉", 18 , "女"},  
        new Object[]{"虎头" , 2 , "男"}  
    };  
    //定义一维数据作为列标题  
    Object[] columnTitle = {"姓名" , "年龄" , "性别"};  
    public void init()  
    {  
        //以二维数组和一维数组来创建一个JTable对象  
        table = new JTable(tableData , columnTitle);  
        //将JTable对象放在JScrollPane中，并将该JScrollPane放在窗口中显示出来  
        jf.add(new JScrollPane(table));  
        jf.pack();  
        jf.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);  
        jf.setVisible(true);  
    }  
     
}  
    
   /* public class SimpleTableTest extends JFrame{

    private static final long serialVersionUID = 1L;
    protected JTable table;
    protected Object[][] data;
    protected String[] colname = {"编号","书名","作者","主角","类别","选择"};
    public SimpleTableTest(){
        Container pane = getContentPane();
        pane.setLayout(new BorderLayout());
        createTableData();  //创建表格所需数据 
        table = getSimpleTable();  
        JScrollPane jsPane = new JScrollPane(table);
        pane.add(jsPane,BorderLayout.CENTER);
    }
    public void createTableData(){
        data = new Object[10][6];
        int i =0;
        data[i++] = new Object[]{};
        data[i++] = new Object[]{};
        data[i++] = new Object[]{};
        data[i++] = new Object[]{};
        data[i++] = new Object[]{};
        data[i++] = new Object[]{};
        data[i++] = new Object[]{};
        data[i++] = new Object[]{};
        data[i++] = new Object[]{};
        data[i++] = new Object[]{};
    }

    /**
     * 返回一个简单的表格
     * @return
     */
   /* public JTable getSimpleTable(){
        table = new JTable(data,colname);
        return table;
    }
}*/
 
} 

