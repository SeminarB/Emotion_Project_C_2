// Fill out your copyright notice in the Description page of Project Settings.

using UnrealBuildTool;
using System.Collections.Generic;

public class Emotion_Project_C_2EditorTarget : TargetRules
{
	public Emotion_Project_C_2EditorTarget(TargetInfo Target) : base(Target)
	{
		Type = TargetType.Editor;

		ExtraModuleNames.AddRange( new string[] { "Emotion_Project_C_2" } );
	}
}
