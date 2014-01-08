/*************************************************************************
 *  Compilation:  javac TestClient.java
 *  Execution:    java TestClient
 *
 *  A bare-bones immutable data type for M-by-N matrices.
 *  Each data element is stored as a "double" data type.
 *
 *************************************************************************/

public class TestClient extends Matrix {



    public TestClient(double[][] data) {
		super(data);
		// TODO Auto-generated constructor stub
	}

	// test client
    public static void main(String[] args) {
 
        int maxNumberOfMatrices = 10000;
        int sizeOfM = 100;
        double c = 2.0 / sizeOfM;
        Matrix[] MatrixArray = new Matrix[maxNumberOfMatrices];
        double percentHeapUsed = 0.0;
        
        Matrix mtxA;
        Matrix mtxB;      
        Matrix mtxC;
        Matrix mtxD;
        
        
        System.out.println();
        System.out.println();
        System.out.println();
        
        
        // Get current size of heap in bytes
        long heapSize = Runtime.getRuntime().totalMemory();

        // Get maximum size of heap in bytes. The heap cannot grow beyond this size.
        // Any attempt will result in an OutOfMemoryException.
        long heapMaxSize = Runtime.getRuntime().maxMemory();
        
        // Calculate percent of available memor
		percentHeapUsed = heapSize / heapMaxSize;

        // Get amount of free memory within the heap in bytes. This size will increase
        // after garbage collection and decrease as new objects are created.
        long heapFreeSize = Runtime.getRuntime().freeMemory();
        

        // Show initial statistics for memory
		System.out.format("HeapSize is %,8d  (or  %f%% used)" + "%n  with  %,8d free.  %n(heapMaxSize is %,8d) %n%n%n", 
				heapSize, percentHeapUsed*100, heapFreeSize, heapMaxSize);
        
        
		
		float startTime = System.nanoTime();    
		float estimatedTime = System.nanoTime() - startTime;
		
		/* CREATE RANDOM ENTRIES INTO MATRICES */
        for (int iii = 0; iii < maxNumberOfMatrices; iii++) {
        	Matrix m_by_n = Matrix.random(sizeOfM,sizeOfM);
        	MatrixArray[iii] = m_by_n;
        	
        }

        
        /*********************/
        // THIS SECTION MULTIPLIES ALL RANDOMLY GENERATED MATRICES WITH EACH OTHER
        //    AND APPLIES A 'SCALAR MULTIPLICATION' AFTER EACH MATRIX MULTIPLICATION
        /*********************/
        mtxC = MatrixArray[0];  
        
        for (int iii=0; iii < maxNumberOfMatrices - 1; iii++) {
        	int jjj = iii+1;
        	
        	/******DEBUGGING OUTPUT********
            System.out.format("iii = %,d%n", iii);
            System.out.format("jjj = %,d%n", jjj);
            */
        	
            mtxA = mtxC.copy();        
        	mtxB = MatrixArray[jjj];
        	mtxC = mtxA.times(mtxB);
        	        	
        	/******DEBUGGING OUTPUT
        	if (mtxA.data[0][0] > 0.1) {
        		System.out.format("%n%nMATRIX A%n");
        		mtxA.show();
        	}
        	*/
        	
        	mtxD = mtxC.scalarmultiply(c);
        	
        	mtxC = mtxD.copy();

        	/*DEBUGGING OUTPUT
        	if (iii % 10 == 0) {
        		
        		
        	}
        	*/
        }
        
		//************
		//OUTPUT MATRIX
		//************
        // mtxC.show();
        
     // print time elapsed
		estimatedTime = System.nanoTime() - startTime;
		System.out.format("Elapsed Time is:  %f seconds.%n%n%n", estimatedTime/1000000000);  

		//************
		//OUTPUT MEMORY INFORMATION
		//************
        System.out.format("    " +
          	     " %,d x %,d matrices created.    (%,d = number of matrices created)%n",
          	                   sizeOfM, sizeOfM, maxNumberOfMatrices); 
              	
   		heapSize = Runtime.getRuntime().totalMemory();
   		heapFreeSize = Runtime.getRuntime().freeMemory();
   		heapMaxSize = Runtime.getRuntime().maxMemory();
   		percentHeapUsed = heapSize / heapMaxSize;
   		
   		System.out.format("HeapSize is %,8d  (or  %f%% used)" + "%n  with  %,8d free.  %n(heapMaxSize is %,8d)%n", 
   							heapSize, percentHeapUsed*100, heapFreeSize, heapMaxSize);

   		
   		
    }
}
