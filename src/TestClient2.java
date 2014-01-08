/*************************************************************************
 *  Compilation:  javac TestClient2.java
 *  Execution:    java TestClient2
 *
 *  A bare-bones immutable data type for M-by-N matrices.
 *  Each data element is stored as a "double" data type.
 *
 *************************************************************************/

public class TestClient2 extends Matrix {



    public TestClient2(double[][] data) {
		super(data);
		// TODO Auto-generated constructor stub
	}

	// test client
    public static void main(String[] args) {
 
    	
    	 

        System.out.println("MATRIX A:  RANDOMIZED 5X5");
        Matrix A = Matrix.random(5, 5);
        A.show(); 
        System.out.println();

        System.out.println("MATRIX B:  TRANSPOSED A");
        Matrix B = A.transpose();
        B.show(); 
        System.out.println();

        System.out.println("MATRIX C:  IDENTITY 5X5");
        Matrix C = Matrix.identity(5);
        C.show(); 
        System.out.println();
        
        System.out.println("MATRIX D:  MATRIX A with SWAPPED ROWS 1 AND 2");
        Matrix D = A.swap(1, 2);
        D.show(); 
        System.out.println();

        System.out.println("A + B");
        A.plus(B).show();
        System.out.println();

        System.out.println("B * A");
        B.times(A).show();
        System.out.println();

        System.out.println("A * B");
        A.times(B).show();
        System.out.println();
        
        // shouldn't be equal since AB != BA in general   
        System.out.println("IS AB = BA ?");
        System.out.println(A.times(B).eq(B.times(A)));
        System.out.println();

        System.out.println("MATRIX b:  RANDOMIZED 5x1");
        Matrix b = Matrix.random(5, 1);
        b.show();
        System.out.println();

        System.out.println("x = A solve b");
        Matrix x = A.solve(b);
        x.show();
        System.out.println();

        System.out.println("A*x");
        A.times(x).show();


   		
    }
}
