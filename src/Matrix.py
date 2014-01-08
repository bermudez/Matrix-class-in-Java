/*************************************************************************
 *  Run command:  python -c Matrix.py
 *  Execution:    java Matrix
 *
 *  A bare-bones immutable data type for M-by-N matrices.
 *  Each data element is stored as a "double" data type.
 *  Most of the source code came from: http://introcs.cs.princeton.edu/java/95linear/Matrix.java.html
 *  Copyright 2000-2011, Robert Sedgewick and Kevin Wayne.
 *  Last updated: Wed Feb 9 09:20:16 EST 2011.
 *************************************************************************/

// import java.io.PrintStream;


/*******CLASS:  Matrix************************************
 * 
 * 		M 	 : private integer; used as the row size
 * 		N 	 : private integer; used as the column size
 * 		data : double[][]
 * 
 * ----------
 * 
 * 		Matrix(int, int)	:Matrix		//create M-by-N matrix of 0's
 * 		Matrix(double[][])	:Matrix		//create matrix based on 2-dimensional array
 * 		Matrix(Matrix)      :Matrix		//copy constructor
 * 		copy()				:Matrix		// return a copy of the matrix
 * 		random(int, int) 	:Matrix     // create and return a random M-by-N matrix with values between 0 and 1
 * 		identity(int)		:Matrix     // create and return the N-by-N identity matrix
 * 		swap(int, int)		:void		// swap rows i and j
 * 		transpose()			:Matrix		// create and return the transpose of the invoking matrix
 * 		plus(Matrix)		:Matrix     // return C = A + B
 * 		minus(Matrix)		:Matrix		// return C = A - B
 * 		eq(Matrix)			:boolean	// does A = B exactly?
 * 		times(Matrix)		:Matrix		// return C = A * B
 * 		multiply(Matrix)	:Matrix		// return C = A * B
 * 		scalarmultiply(double)	:Matrix		// return C = double_x * B 
 * 		solve(Matrix)		:Matrix		// return x = A^-1 b, assuming A is square and has full rank
 * 		show()				:void		// print matrix to standard output
 * 		randomlySelectRows(Matrix, int)	:Matrix		//useful for bootstrapping
 * 		averageMatrix(Matrix)  : Matrix	//returns a 1xN vector matrix of sample means
 * 		residualsMatrix(Matrix): Matrix	// Returns the MxN matrix of residuals (given a sample depicted in the MxN matrix)
 * 		squaredResidualsMatrix(Matrix) :Matrix		// Returns the MxN matrix of squared residuals (given a sample depicted in the MxN matrix)
 * 		varianceMatrix(Matrix) :Matrix	// Returns the 1xN matrix of variances (given a sample depicted in the MxN matrix)
 * 		covarianceMatrix(Matrix) :Matrix  // Returns the MxN matrix of covariances (given a sample depicted in the MxN matrix)
 * 
 */

public class Matrix {
    public int M;             // number of rows
    public int N;             // number of columns
    public double[][] data;   // M-by-N array

    // create M-by-N matrix of 0's
    public Matrix(int M, int N) {
        this.M = M;
        this.N = N;
        data = new double[M][N];
    }

    // create matrix based on 2d array
    public Matrix(double[][] data) {
        M = data.length;
        N = data[0].length;
        this.data = new double[M][N];
        for (int i = 0; i < M; i++)
            for (int j = 0; j < N; j++)
                    this.data[i][j] = data[i][j];
    }

    // copy constructor
    private Matrix(Matrix A) { this(A.data); }
    
    // return copy of matrix
    public Matrix copy() {
        Matrix A = this;
        Matrix C = new Matrix(A.M, A.N);
        for (int i = 0; i < C.M; i++)
            for (int j = 0; j < C.N; j++)
                C.data[i][j] = (A.data[i][j]);
        return C;
    }

    // create and return a random M-by-N matrix with values between 0 and 1
    public static Matrix random(int M, int N) {
        Matrix A = new Matrix(M, N);
        for (int i = 0; i < M; i++)
            for (int j = 0; j < N; j++)
                A.data[i][j] = Math.random();
        return A;
    }

    // create and return the N-by-N identity matrix
    public static Matrix identity(int N) {
        Matrix I = new Matrix(N, N);
        for (int i = 0; i < N; i++)
            I.data[i][i] = 1;
        return I;
    }

    // swap rows i and j
    public Matrix swap(int i, int j) {
        Matrix A = this.copy();
        double[] tempi = this.data[i];
        double[] tempj = this.data[j];
        A.data[i] = tempj;
        A.data[j] = tempi;
        return A;
    }

    // create and return the transpose of the invoking matrix
    public Matrix transpose() {
        Matrix A = new Matrix(N, M);
        for (int i = 0; i < M; i++)
            for (int j = 0; j < N; j++)
                A.data[j][i] = this.data[i][j];
        return A;
    }

    // return C = A + B
    public Matrix plus(Matrix B) {
        Matrix A = this;
        if (B.M != A.M || B.N != A.N) throw new RuntimeException("Illegal matrix dimensions.");
        Matrix C = new Matrix(M, N);
        for (int i = 0; i < M; i++)
            for (int j = 0; j < N; j++)
                C.data[i][j] = A.data[i][j] + B.data[i][j];
        return C;
    }

    // return C = A - B
    public Matrix minus(Matrix B) {
        Matrix A = this;
        if (B.M != A.M || B.N != A.N) throw new RuntimeException("Illegal matrix dimensions.");
        Matrix C = new Matrix(M, N);
        for (int i = 0; i < M; i++)
            for (int j = 0; j < N; j++)
                C.data[i][j] = A.data[i][j] - B.data[i][j];
        return C;
    }

    // does A = B exactly?
    public boolean eq(Matrix B) {
        Matrix A = this;
        if (B.M != A.M || B.N != A.N) throw new RuntimeException("Illegal matrix dimensions.");
        for (int i = 0; i < M; i++)
            for (int j = 0; j < N; j++)
                if (A.data[i][j] != B.data[i][j]) return false;
        return true;
    }

    // return C = A * B
    public Matrix times(Matrix B) {
        Matrix C = new Matrix(this.M, B.N);
        for (int i = 0; i < this.M; i++) {
            double[] arowi = this.data[i];
            double[] crowi = C.data[i];
            for (int k = 0; k < B.N; k++) {
                double[] browk = B.data[k];
                double aik = arowi[k];
                for (int j = 0; j < N; j++) {
                    crowi[j] += aik * browk[j];
                }
            }
        }
        return C;
    }
    
    // return C = A * B
    public Matrix multiply(Matrix B) {
        Matrix C = new Matrix(this.M, B.N);
        for (int i = 0; i < this.M; i++) {
            double[] arowi = this.data[i];
            double[] crowi = C.data[i];
            for (int k = 0; k < B.N; k++) {
                double[] browk = B.data[k];
                double aik = arowi[k];
                for (int j = 0; j < N; j++) {
                    crowi[j] += aik * browk[j];
                }
            }
        }
        return C;
    }
    
    //ALTERNATIVE MULTIPLICATION ALGORITHM
    /*
    public Matrix multiply(Matrix B) {
    
        Matrix A = this;
        if (A.N != B.M) throw new RuntimeException("Illegal matrix dimensions.");
        Matrix C = new Matrix(A.M, B.N);
        for (int i = 0; i < C.M; i++)
            for (int j = 0; j < C.N; j++)
                for (int k = 0; k < A.N; k++)
                    C.data[i][j] += (A.data[i][k] * B.data[k][j]);
        return C;
    }
	*/    

    // return C = x * B
    public Matrix scalarmultiply(double c) {
        Matrix C = new Matrix(this.M, this.N);
        for (int i = 0; i < this.M; i++)
            for (int j = 0; j < this.N; j++)
            	C.data[i][j] = (c * this.data[i][j]);
        return C;
    }

    // return x = A^-1 b, assuming A is square and has full rank
    public Matrix solve(Matrix rhs) {
        if (M != N || rhs.M != N || rhs.N != 1)
            throw new RuntimeException("Illegal matrix dimensions.");

        // create copies of the data
        Matrix A = new Matrix(this);
        Matrix b = new Matrix(rhs);

        // Gaussian elimination with partial pivoting
        for (int i = 0; i < N; i++) {

            // find pivot row and swap
            int max = i;
            for (int j = i + 1; j < N; j++)
                if (Math.abs(A.data[j][i]) > Math.abs(A.data[max][i]))
                    max = j;
            A.swap(i, max);
            b.swap(i, max);

            // singular
            if (A.data[i][i] == 0.0) throw new RuntimeException("Matrix is singular.");

            // pivot within b
            for (int j = i + 1; j < N; j++)
                b.data[j][0] -= b.data[i][0] * A.data[j][i] / A.data[i][i];

            // pivot within A
            for (int j = i + 1; j < N; j++) {
                double m = A.data[j][i] / A.data[i][i];
                for (int k = i+1; k < N; k++) {
                    A.data[j][k] -= A.data[i][k] * m;
                }
                A.data[j][i] = 0.0;
            }
        }

        // back substitution
        Matrix x = new Matrix(N, 1);
        for (int j = N - 1; j >= 0; j--) {
            double t = 0.0;
            for (int k = j + 1; k < N; k++)
                t += A.data[j][k] * x.data[k][0];
            x.data[j][0] = (b.data[j][0] - t) / A.data[j][j];
        }
        return x;
   
    }

    // print matrix to standard output
    public void show() {
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) 
                System.out.printf("%9.4f ", data[i][j]);
            System.out.println();
        }
    }
}
