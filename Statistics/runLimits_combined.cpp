
#include "MC_Bayes.cpp+"

{

  Int_t Nmasses;
  Int_t Nchannels;
  Int_t mass;
  Double_t dummy;

  ifstream input("inputs_bothChannels.txt");
  
  input >> Nmasses;
  input >> Nchannels;

  Double_t* masses = new Double_t[Nmasses];

  Double_t** bkg = new Double_t*[Nmasses];
  for (int i = 0; i < Nmasses; i++)
    bkg[i] = new Double_t[Nchannels];
  Double_t** bkgUncertainty = new Double_t*[Nmasses];
  for (int i = 0; i < Nmasses; i++)
    bkgUncertainty[i] = new Double_t[Nchannels];
  Double_t** efficiency = new Double_t*[Nmasses];
  for (int i = 0; i < Nmasses; i++)
    efficiency[i] = new Double_t[Nchannels];
  Double_t** efficiencyUncertainty = new Double_t*[Nmasses];
  for (int i = 0; i < Nmasses; i++)
    efficiencyUncertainty[i] = new Double_t[Nchannels];
  Double_t** Nsignal = new Double_t*[Nmasses];
  for (int i = 0; i < Nmasses; i++)
    Nsignal[i] = new Double_t[Nchannels];
  Int_t** Nobs = new Int_t*[Nmasses];
  for (int i = 0; i < Nmasses; i++)
    Nobs[i] = new Int_t[Nchannels];


  for (mass = 0; mass < Nmasses; mass++) {
    input >> masses[mass];
    input >> dummy;
    
    for (Int_t chan = 0; chan < Nchannels; chan++) {
      input >> efficiency[mass][chan];
      input >> efficiencyUncertainty[mass][chan];
      input >> Nsignal[mass][chan]; 
      input >> bkg[mass][chan];
      input >> bkgUncertainty[mass][chan];
      input >> Nobs[mass][chan];
    }
  }


  ofstream outputFile("limits.txt");

  for (mass = 0; mass < Nmasses; mass++) {

    cout << "\n----------------------------\n";
    cout << "mass = " << masses[mass] << " GeV:" << endl;
    
    Double_t intLum = 20.28;
    Double_t intLumUncertainty = intLum*0.028;

    cout << "\nInputs:\n";
    cout << "Int. luminosity = (" << intLum << " +/- " << intLumUncertainty << ")/fb\n";
    
      
    Double_t* background = new Double_t[Nchannels];
    for (int chan = 0; chan < Nchannels; chan++)
      background[chan] = bkg[mass][chan]/intLum;
    
    Double_t* backgroundUncertainty = new Double_t[Nchannels];
    for (int chan = 0; chan < Nchannels; chan++)
      backgroundUncertainty[chan] = bkgUncertainty[mass][chan]/intLum;
    
    Int_t* Nobserved = new Int_t[Nchannels];
    for (int chan = 0; chan < Nchannels; chan++)
      Nobserved[chan] = Nobs[mass][chan];

    Double_t* signalEfficiency = new Double_t[Nchannels];
    for (int chan = 0; chan < Nchannels; chan++)
      signalEfficiency[chan] = efficiency[mass][chan];
    
    Double_t* signalEfficiencyUncertainty = new Double_t[Nchannels];
    for (int chan = 0; chan < Nchannels; chan++)
      signalEfficiencyUncertainty[chan] = efficiencyUncertainty[mass][chan];

    
    for (int chan = 0; chan < Nchannels; chan++) {
      cout << "Channel " << chan << ":\n";
      cout << "   Background = " << bkg[mass][chan] << " +/- " << bkgUncertainty[mass][chan] << endl;
      cout << "   Observed events = " << Nobs[mass][chan] << endl;
      cout << "   Signal efficiency = " << efficiency[mass][chan] << " +/- " << efficiencyUncertainty[mass][chan] << endl;
    }

	  
    Int_t Nmc = 5000;


    MC_Bayes* mcb = new MC_Bayes(Nchannels, intLum, intLumUncertainty, background, backgroundUncertainty, Nobserved, Nmc, signalEfficiency, signalEfficiencyUncertainty, 
				   false,true,true,true);

    Double_t step = 1.e100;
    for (int chan = 0; chan < Nchannels; chan++) {
      Double_t approxLimitEvts = 1.6 * TMath::Sqrt(bkgUncertainty[mass][chan]*bkgUncertainty[mass][chan] + bkg[mass][chan]);
      if (approxLimitEvts < 3.0)
	approxLimitEvts = 3.0;
      Double_t thisStep = approxLimitEvts/(efficiency[mass][chan]*intLum)/500.0;
      if (thisStep < step)
	step = thisStep;
    }
    
    Double_t limit = mcb->excludedSignal(step, false);
	
    cout << "\nObserved limit: " << limit << " fb" << endl;
    
    cout << "Observed limit / step = " << limit/step << endl;


    step /= 2.0;
    mcb->Nmc = 1000;
    Double_t* exp = mcb->expectedExclusion(step,1000,false);

    cout << "\nExpected limit and bands [fb]:\n";
    cout << "-2sigma     -1sigma     median    +1sigma     +2sigma\n";
    cout << exp[0] << "     " << exp[1] << "     " << exp[2] << "     " << exp[3] << "     " << exp[4] << endl;

    
    outputFile << masses[mass] << " " << Nsignal[mass][0]/(efficiency[mass][0]*intLum) << " " << limit;
    for (Int_t k = 0; k < 5; k++)
      outputFile << " " << exp[k];
    outputFile << endl;

    delete mcb;
    delete[] exp;
  }
  cout << endl;

  outputFile.close();

  delete[] masses;
  delete[] bkg;
  delete[] bkgUncertainty;
  delete[] efficiency;
  delete[] efficiencyUncertainty;
  delete[] Nsignal;
  delete[] Nobs;
}


